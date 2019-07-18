var timeSpan = "max";
sortBy = "noSort";
var data;

$.ajax({
  url: "./data/data.json",
  success: function(result) {
    data = result;
    renderRows();
  }
});

function renderRows() {
  if (sortBy != "noSort") {
    if (sortBy == "roi" || sortBy == "r2") {
      data.sort(function(a, b) {
        return b[timeSpan][sortBy] - a[timeSpan][sortBy];
      });
    } else {
      data.sort(function(a, b) {
        return a[sortBy].toLowerCase().localeCompare(b[sortBy].toLowerCase());
      });
    }
  }
  $("tbody").empty();
  for (i = 0; i < data.length; i++) {
    id = "";
    if (i == 0) {
      id = "id='firstRow'";
    }
    if (i == data.length - 1) {
      id = "id='lastRow'";
    }
    stock = data[i];
    $("tbody").append(
      "<tr " +
        id +
        "><th class='symbols'>" +
        stock.symbol +
        "</th><td class='company'>" +
        stock.company +
        "</td><td class='roi'>" +
        round(stock[timeSpan].roi, 100) +
        "%</td><td class='r2'>" +
        round(stock[timeSpan].r2, 10000) +
        "</td><td>y = " +
        round(stock[timeSpan].scalar, 100) +
        "(" +
        round(1 + stock[timeSpan].roi / 100, 1000) +
        ")<sup>x</sup>" +
        "</td><td class='imgHolder'><img src='./images/" +
        stock.symbol.toLowerCase() +
        "_" +
        timeSpan +
        ".png'></img></td></tr>"
    );
  }
}

function round(num, offset) {
  return Math.round(num * offset) / offset;
}

$(".selectable").click(function() {
  $("thead th").removeClass("selected");
  $(this).addClass("selected");
  sortBy = $(this)
    .text()
    .toLowerCase()
    .trim();
  renderRows();
});

$("h4").click(function() {
  $("h4").removeClass("selected");
  $(this).addClass("selected");
  timeSpan = $(this)
    .text()
    .toLowerCase();
  if (sortBy == "company" || sortBy == "symbol") {
    sortBy = "noSort";
  }
  renderRows();
});
