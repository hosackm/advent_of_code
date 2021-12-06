package main

// CountFish uses an array to hold the number of fish of each age
// The only ages possible are 0-8 (inclusive).  After each day
// we shift the number of fish down to the age (index) 1 below
// for fish that were age 0, we add a new fish to age 6 (respawn)
// and add a fish to age 8 (spawn a new fish)
func CountFish(ages []int, days int) int {
	counter := make([]int, SPAWN_AGE+1)

	for i := 0; i <= SPAWN_AGE; i++ {
		counter[i] = 0
	}

	for _, a := range ages {
		counter[a]++
	}

	for d := 0; d < days; d++ {
		numRespawns := counter[0]
		counter[0] = counter[1]
		counter[1] = counter[2]
		counter[2] = counter[3]
		counter[3] = counter[4]
		counter[4] = counter[5]
		counter[5] = counter[6]
		counter[6] = counter[7] + numRespawns
		counter[7] = counter[8]
		counter[8] = numRespawns
	}

	count := 0
	for _, v := range counter {
		count += v
	}

	return count
}
