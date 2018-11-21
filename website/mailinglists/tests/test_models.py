from django.core.exceptions import ValidationError
from django.test import TestCase

from mailinglists.models import MailingList, ListAlias


class MailingListTest(TestCase):
    """Tests mailing lists"""

    @classmethod
    def setUpTestData(cls):
        cls.mailinglist = MailingList.objects.create(
            name="mailtest",
        )

    def setUp(self):
        self.mailinglist.refresh_from_db()

    def test_clean_works(self):
        self.mailinglist.clean()

    def test_no_alias_duplicates(self):
        listalias = ListAlias(
            alias="mailtest",
            mailinglist=self.mailinglist
        )

        with self.assertRaises(ValidationError):
            listalias.clean()

        listalias.alias = "mailalias"
        listalias.clean()

    def test_no_automatic_list(self):
        mailinglist = MailingList(
            name="activemembers"
        )

        with self.assertRaises(ValidationError):
            mailinglist.clean()

        mailinglist.name = "activemembers1"
        mailinglist.clean()

    def test_autoresponse_has_text(self):
        self.mailinglist.autoresponse_enabled = True

        with self.assertRaises(ValidationError):
            self.mailinglist.clean()

        self.mailinglist.autoresponse_text = "Hello World"
        self.mailinglist.clean()


class ListAliasTest(TestCase):
    """Tests list aliases"""

    @classmethod
    def setUpTestData(cls):
        cls.mailinglist = MailingList.objects.create(
            name="mailtest",
        )
        cls.listalias = ListAlias.objects.create(
            alias="mailalias",
            mailinglist=cls.mailinglist
        )

    def setUp(self):
        self.mailinglist.refresh_from_db()
        self.listalias.refresh_from_db()

    def test_clean_works(self):
        self.listalias.clean()

    def test_no_automatic_list(self):
        listalias = ListAlias(
            alias="activemembers",
            mailinglist=self.mailinglist
        )

        with self.assertRaises(ValidationError):
            listalias.clean()

    def test_no_mailinglist_duplicates(self):
        m1 = MailingList(
            name="mailalias"
        )

        with self.assertRaises(ValidationError):
            m1.clean()

        m1.name = "mailtest2"
        m1.clean()
