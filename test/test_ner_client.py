import unittest

from parameterized import parameterized

from ner_client import NamedEntityClient
from test_doubles import NerModelTestDoubles


class TestNerClient(unittest.TestCase):

    def test_givenEmptyString_whenGetEnts_thenReturnDict(self):
        model = NerModelTestDoubles('eng')
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ent = ner.get_entities("")
        self.assertIsInstance(ent, dict)

    def test_givenString_whenGetEnts_thenReturnDict(self):
        model = NerModelTestDoubles('eng')
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ent = ner.get_entities("Madison is a city in Wisconsin")
        self.assertIsInstance(ent, dict)

    def test_givenModel_whenCallSpacy_PERSON_thenReturnSerializedPerson(self):
        model = NerModelTestDoubles('eng')
        doc_ents = [{"text": "Laurent Fressinet", "label_": "PERSON"}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_entities("...")
        expected_result = {"ents": [{"ent": "Laurent Fressinet", "label": "Person"}], "html": ""}
        self.assertListEqual(result["ents"], expected_result["ents"])

    def test_givenModel_whenCallSpacy_NORP_thenReturnGroup(self):
        model = NerModelTestDoubles('eng')
        doc_ents = [{"text": "Lithuanian", "label_": "NORP"}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_entities("...")
        expected_result = {"ents": [{"ent": "Lithuanian", "label": "Group"}], "html": ""}
        self.assertListEqual(result["ents"], expected_result["ents"])

    @parameterized.expand(((
            ("Laurent Fressinet", "PERSON", "Person"),
            ("Lithuanian", "NORP", "Group"),
            ("the ocean", "LOC", "Location"),
            ("ASL", "LANGUAGE", "Language"),
            ("Australia", "GPE", "Location"),
    )))
    def test_givenModel_whenCallSpacy_thenReturnGroup(self, text, label, expected):
        model = NerModelTestDoubles('eng')
        doc_ents = [{"text": text, "label_": label}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_entities("...")
        expected_result = {"ents": [{"ent": text, "label": expected}], "html": ""}
        self.assertListEqual(result["ents"], expected_result["ents"])
