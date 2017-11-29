from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.utils import translation
from django.utils.translation import ugettext_lazy as _

from events.models import Registration
from members.models import Profile
from thaliawebsite.templatetags import baseurl


def notify_first_waiting(request, event):
    if (event.max_participants is not None and
        Registration.objects
                    .filter(event=event, date_cancelled=None)
                    .count() > event.max_participants):
        # Prepare email to send to the first person on the waiting list
        first_waiting = (Registration.objects
                         .filter(event=event, date_cancelled=None)
                         .order_by('date')[event.max_participants])
        first_waiting_member = first_waiting.member

        text_template = get_template('events/member_email.txt')

        if first_waiting_member.profile:
            language = first_waiting_member.member.language
        else:
            language = Profile._meta.get_field('language').default

        with translation.override(language):
            subject = _("[THALIA] Notification about your "
                        "registration for '{}'").format(
                event.title)
            text_message = text_template.render({
                'event': event,
                'reg': first_waiting,
                'member': first_waiting_member,
                'base_url': baseurl.baseurl(context={'request': request})
            })

            EmailMessage(
                subject,
                text_message,
                to=[first_waiting_member.email]
            ).send()


def notify_organiser(event, registration):
    if event.organiser is None or event.organiser.contact_mailinglist is None:
        return

    text_template = get_template('events/organiser_email.txt')
    subject = 'Registration for {} cancelled by member'.format(
        event.title)
    text_message = text_template.render({
        'event': event,
        'registration': registration
    })

    EmailMessage(
        subject,
        text_message,
        to=[event.organiser.contact_mailinglist.name + "@thalia.nu"]
    ).send()