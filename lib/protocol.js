var data = [],
    dataMap = {},
    dataIndex = 0,
    width = 900,
    height = 400,
    total = 0,
    svg;

function addData(newData) {
  total += newData.length;

  for(var i=0; i < newData.length; i++) {
    var cur = newData[i];
    if (dataMap[newData[i]] == undefined) {
      dataMap[newData[i]] = {count:1, index: dataIndex};
      data[dataIndex] = dataMap[newData[i]];
      dataIndex++;
    }
   else {
      dataMap[newData[i]].count++;
   }
  }
};

function update() {
  var circle = svg.selectAll("circle");

  //enter
  circle.enter().append("circle")
    .attr("cy", height/2)
    .attr("cx", function(d, i) { return width/(i * data.length + 2); });

  //update
  circle
    .attr("r", function(d) { return 30 * (d.count/total) + 2; });
}

function poll() {
  $.ajax({
    type: "GET",
    url: "data",
    cache: false,
    timeout: 50000,
    dataType: "json",

    success: function(data) {
      addData(data);
      update();
      setTimeout(poll,
        500);
    },

    error: function(xhr, status, error) {
      console.log(xhr, status, error);
    }

  });

};
  
$(document).ready(function() {
  svg = d3.select("body")
    .append("svg")
    .attr("wdith", width)
    .attr("height", height);

  poll();
});
