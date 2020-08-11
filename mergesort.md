const split =
	array => {
		const midpoint = Math.floor(array.length / 2)
		return [array.slice(0, midpoint), array.slice(midpoint, array.length)]
	}

// ugh
const merge =
	([a, b]) => {

		const c = new Array(a.length + b.length)

		let i   = 0
		let ii  = 0

		for (let iii = 0; iii < c.length; ++iii) {
			if ((a[i] || Infinity) <= (b[ii] || Infinity))
				c[iii] = a[i++]
			else
				c[iii] = b[ii++]
		}

		return c

	}

const mergesort =
	array =>
		array.length <= 1
			? array
			: merge(split(array).map(mergesort))

console.log(mergesort([6000, 1, 2, 3, 17, 176, 17, 601, -10, 4, 10,9,9,1,1,1,9,9,9,9,9,9, 5, 6, -50]))