'''
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다.
지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.
체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로
칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.
보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8*8 크기는
아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
'''

n, m = map(int, input().split())
board = []
for _ in range(n):
	board.append(input())

def invalid_count(str1, str2):
	cnt = 0
	for i in range(len(str1)):
		if str1[i] != str2[i]:
			cnt += 1

	return cnt

def eight_by_count(board):
	check_w = "WBWBWBWB"
	check_b = "BWBWBWBW"

	cnt1, cnt2 = 0, 0
	for i in range(8):
		if i % 2 == 0:
			cnt1 += invalid_count(check_w, board[i])
		else :
			cnt1 += invalid_count(check_b, board[i])

	for i in range(8):
		if i % 2 == 0:
			cnt2 += invalid_count(check_b, board[i])
		else :
			cnt2 += invalid_count(check_w, board[i])
	return min(cnt1, cnt2)

def solution(board, n, m):

	ans = []
	cnt = 0
	for k in range(n - 7):
		for j in range(m - 7):
			new_board = []
			for i in range(8):
				new_board.append(board[i + k][j : j + 8])
			ans.append(eight_by_count(new_board))

	return min(ans)

print(solution(board, n, m))
