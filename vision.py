from detecto import core, utils, visualize


def filtering_by_score(scores, labels, max_score = 0.7):
    """"Upgrade -> Filtering by score >= 0.7"""
    aux_label = []
    aux_scores = []

    index = 0

    for value in scores:
        if value > max_score:
            aux_label.append(labels[index])
            aux_scores.append(value)
        index += 1

    print(aux_label)
    print(aux_scores)
    print("\n")


# Importar la imagen para analizar
image = utils.read_image('./resources/prueba2.jpg')

# Importar modelo preentrenado - Coco Dataset
model = core.Model()


# Detección de todos los objetos
labels, boxes, scores = model.predict(image)

print(labels)
print(scores)
print("\n")

visualize.show_labeled_image(image, boxes, labels)

filtering_by_score(scores, labels, max_score = 0.7)


# Detección del principal elemento para cada etiqueta / label
labels, boxes, scores = model.predict_top(image)

print(labels)
print(scores)
print("\n")

visualize.show_labeled_image(image, boxes, labels)

filtering_by_score(scores, labels, max_score = 0.7)