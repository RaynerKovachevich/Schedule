function toggleVisibility(column) {
    var columnElement = document.querySelectorAll("." + column + "2");
    columnElement.forEach(function (element) {
        if (element.style.display === "none" || element.style.display === "") {
            element.style.display = "table-cell";
        } else {
            element.style.display = "none";
        }
    });
}


function resetVisibility() {
    var allElements = document.querySelectorAll(".time2, .event2");
    allElements.forEach(function (element) {
        element.style.display = "none";
    });
}


