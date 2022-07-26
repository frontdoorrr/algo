# def solution(prices):
# 	answer = [0] * len(prices)
# 	while prices:
# 		price = prices.pop()
# 		for i in range(len(prices)):
# 			if prices[i] <= price:
# 				answer[i] += 1
# 	return answer

def solution(prices):
	t, l= 0, 0
	tmp = 0
	ans = []
	while prices:
		price = prices.pop()
		if price < tmp:
			ans.append(t)
			l += 1
		else :
			ans.append(t - l)
			l = 0
			tmp = price
		t += 1
	return sorted(ans, reverse=True)

ps = [1, 2, 3, 2, 3]
print("answer :", solution(ps))
