# src/graph/entity_extractor.py

import spacy

nlp = spacy.load("en_core_web_sm")


def extract_entities(text):
    """
    Extract named entities from text
    """
    doc = nlp(text)
    entities = set()

    for ent in doc.ents:
        if ent.label_ in {"PERSON", "ORG", "GPE", "NORP", "EVENT", "LAW"}:
            entities.add(ent.text.strip())

    return list(entities)


def extract_relations(text):
    """
    Simple dependency-based relation extraction
    """
    doc = nlp(text)
    relations = []

    for sent in doc.sents:
        subject = None
        verb = None
        obj = None

        for token in sent:
            if "subj" in token.dep_:
                subject = token.text
            elif token.pos_ == "VERB":
                verb = token.lemma_
            elif "obj" in token.dep_:
                obj = token.text

        if subject and verb and obj:
            relations.append((subject, verb, obj))

    return relations
