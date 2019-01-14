## Java Script - d3 :hugs:

> **D3** (or **D3.js**) is a JavaScript library for visualizing data using web standards. D3 helps you bring data to life using SVG, Canvas and HTML. D3 combines powerful visualization and interaction techniques with a data-driven approach to DOM manipulation, giving you the full capabilities of modern browsers and the freedom to design the right visual interface for your data.

[https://github.com/d3/d3](https://github.com/d3/d3)

---
### selection
[API reference](https://github.com/d3/d3-selection)
selection methods that return the current selection use _four_ spaces of indent, while methods that return a new selection use only _two_.

		d3.select("body")
		  .append("svg")
		    .attr("width", 960)
		    .attr("height", 500)
		  .append("g")
		    .attr("transform", "translate(20,20)")
		  .append("rect")
		    .attr("width", 920)
		    .attr("height", 460);
Selection methods accept [W3C selector strings](http://www.w3.org/TR/selectors-api/) such as `.fancy` to select elements with the class _fancy_, or `div` to select DIV elements.  
Selection methods come in two forms: select and selectAll: the former selects only the first matching element, while the latter selects all matching elements in document order.   
The top-level selection methods, [d3.select](https://github.com/d3/d3-selection#select) and [d3.selectAll](https://github.com/d3/d3-selection#selectAll), query the entire document; the subselection methods, [_selection_.select](https://github.com/d3/d3-selection#selection_select) and [_selection_.selectAll](https://github.com/d3/d3-selection#selection_selectAll), restrict selection to descendants of the selected elements.		


		//to select the first bold element in every paragraph
		var b = d3.selectAll("p").select("b");

### modifying elements
After selecting elements, use the selection’s transformation methods to affect document content. 

	// to set the name attribute and color style of an anchor element
	d3.select("a")
	    .attr("name", "fred")
	    .style("color", "red");

### joining Data
The _data_ is specified **for each group** in the selection. If the selection has multiple groups (such as [d3.selectAll](https://github.com/d3/d3-selection#selectAll) followed by [_selection_.selectAll](https://github.com/d3/d3-selection#selection_selectAll)), then _data_ should typically be specified as a function. This function will be evaluated for each group in order, being passed the group’s parent datum (_d_, which may be undefined), the group index (_i_), and the selection’s parent nodes (_nodes_), with _this_ as the group’s parent element. 

	// Create an HTML table from a matrix of numbers:
	var matrix = [
	  [11975,  5871, 8916, 2868],
	  [ 1951, 10048, 2060, 6171],
	  [ 8010, 16145, 8090, 8045],
	  [ 1013,   990,  940, 6907]
	];

	var tr = d3.select("body")
	  .append("table")
	  .selectAll("tr")
	  .data(matrix)
	  .enter().append("tr");

	var td = tr.selectAll("td")
	  .data(function(d) { return d; })
	  .enter().append("td")
	    .text(function(d) { return d; });
	    
[#](https://github.com/d3/d3-selection#selection_enter)  _selection_.**enter**()  [<>](https://github.com/d3/d3-selection/blob/master/src/selection/enter.js "Source")

Returns the enter selection: placeholder nodes for each datum that had no corresponding DOM element in the selection. (The enter selection is empty for selections not returned by  [_selection_.data](https://github.com/d3/d3-selection#selection_data).)

The enter selection is typically used to create “missing” elements corresponding to new data. For example, to create DIV elements from an array of numbers:

	var div = d3.select("body")
	  .selectAll("div")
	  .data([4, 8, 15, 16, 23, 42])
	  .enter().append("div")
	    .text(function(d) { return d; });
If the body is initially empty, the above code will create six new DIV elements, append them to the body in-order, and assign their text content as the associated (string-coerced) number:

	<div>4</div>
	<div>8</div>
	<div>15</div>
	<div>16</div>
	<div>23</div>
	<div>42</div>
