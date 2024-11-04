import spacy


class NamedEntityClient:
    def __init__(self, model):
        self.model = model

    def get_entities(self, sentence):
        doc = self.model(sentence)
        entities = [{'ent': ent.text, "label": self.map_label(ent.label_)} for ent in doc.ents]
        return {"ents": entities, "html": ""}

    @staticmethod
    def map_label(label):
        label_map = {
            'PERSON': 'Person',
            'NORP': 'Group',
        }
        return label_map.get(label)
