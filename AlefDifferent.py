from funcs import trapezoids, triangle, pyramid, length, median

def questions(selectedQ, quantity):
    text = ""
    if selectedQ == "Trapezoid":
        text = trapezoids.trapezoids(quantity)
    elif selectedQ == "Triangle":
        text = triangle.triangle(quantity)
    elif selectedQ == "Pyramid":
        text = pyramid.pyramids(quantity)
    elif selectedQ == "Length":
        text = length.length(quantity)
    elif selectedQ == "Median":
        text = median.median(quantity)

    return text