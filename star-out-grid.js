function findStarCoordinates(grid, star) {
	let star_locs = [];

	// find the coordinates of stars and put them into array
	for (let row of grid) {
		let found_row;
		let found_col;
		if (row.indexOf(star) >= 0) {
			found_row = grid.indexOf(row);
			found_col = row.indexOf(star);
			star_locs.push([found_row, found_col]);
		}
	}
	return star_locs;
}

function starOutGrid(grid, star = "*") {
	// search and replace values with stars in same row and column
	function searchAndReplace(star_loc) {
		for (let [row_id, row] of grid.entries()) {
			if (row_id == star_loc[0]) {
				row.forEach((col, index) => {
					row[index] = "*";
				});
			}
			row[star_loc[1]] = "*";
		}
	}

	// create an array of all star location coordinates
	let star_locs = findStarCoordinates(grid, star);

	// for each coordinate point in array, run the search-and-replace function
	for (let star_loc of star_locs) {
		searchAndReplace(star_loc);
	}

	return grid;
}
