def solution(money, costs):
	answer = 0
	cost_arr = [[1],[5],[10],[50],[100],[500]]

	for i in range(len(costs)):
		cost_arr[i].append(costs[i])
		cost_arr[i].append(cost_arr[i][1] / cost_arr[i][0])

	cost_arr = sorted(cost_arr, key=lambda x: x[2])

	ans  = 0
	amount = 0

	for coin, cost, ratio in cost_arr:
		while amount != money:
			if money - amount >= coin:
				amount += coin
				ans += cost
			elif money - amount < coin:
				break

	return ans


# print(solution(4578, [1,4,99,35,50,1000]))
print(solution(1999,[2,11,20,100,200,600]))
