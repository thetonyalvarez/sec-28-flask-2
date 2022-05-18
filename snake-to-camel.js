function snakeToCamel(str) {
	let split_str = str.split("_");

	let result = split_str[0];

	// start at index 1 because we don't want to affect first split str item (at 0-index)
	for (let i = 1; i < split_str.length; i++) {
		split_str[i] = split_str[i][0].toUpperCase() + split_str[i].slice(1);
		result = result.concat(split_str[i]);
	}
	return result;
}
