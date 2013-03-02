var data = [],
    dataMap = {},
    dataIndex = 0,
    width = 300,
    height = 400
    svg;

function addData(newData) {
  for(var i=0; i < newData.length; i++) {
    if (dataMap[newData[i]] == undefined) {
      dataMap[newData[i]] = {count:1, index: dataIndex};
      data[dataIndex] = dataMap[newData[i]]
      dataIndex++;
    }
   else {
      data[newData[i].index].count++;
   }
  }
};

function update() {

  //enter
  svg.selectAll("circle").enter()
    .append("circle")
    .attr("cy", 200)
    .attr("cx", function(d, i) { return width/(i * data.length); });

  //update
  svg.selectAll("circle")
    .attr("r", function(d) { return Math.ceil(8, d.count * d.count); });
}

function poll() {
  $.ajax({
    type: "GET",
    url: "/data",
    cache: false,
    timeout: 50000,
    dataType: "json"

    success: function(data) {
      addData(data);
      update();
      setTimeout(poll,
        500);
    }

  });

};
  
$(document).ready({function() {
  svg = d3.select("body")
    .append("svg")
    .attr("wdith", width)
    .attr("height", height);

  poll();
  };
});
