var timeSpan = "max";
sortBy = "noSort";
var data;

$.ajax({
  url: "./data_full.json",
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
        "</td><td>" +
        // some chart will go here
        "</td></tr>"
    );
  }
}

function round(num, precision) {
  return Math.round(num * offset) / precision;
}

function getChartWidget(symbol) {
  return (
    '<div class="tradingview-widget-container"><div class="tradingview-widget-container__widget"></div><div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/FX-EURUSD/" rel="noopener" target="_blank"><span class="blue-text">EURUSD Rates</span></a> by TradingView</div><script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>{"symbol": ' +
    symbol +
    ',"width": 350,"height": 220,"locale": "en","dateRange": "12m","colorTheme": "light","trendLineColor": "#37a6ef","underLineColor": "#e3f2fd","isTransparent": false,"autosize": false,"largeChartUrl": ""}</script></div>'
  );
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
