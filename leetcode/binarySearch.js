function binarySearch(input, target) {
	return recur(input, 0, input.length - 1, target);
}

function recur(input, low, high, target) {
	if(low > high){
		console.log("no target is found")
		return false;
	}
	var mid = Math.floor(low + high) /2
	if(input[mid] == target){
		console.log("found target: ", target);
		return true
	}else if(input[mid] > target){
		return recur(input,low,mid - 1,target)
	}else{
		return recur(input,mid+1, high, target)
	}
}

var test = [23,54,67,69,123,124,333,777,899,1000,1002,1010]
binarySearch(test, 22)