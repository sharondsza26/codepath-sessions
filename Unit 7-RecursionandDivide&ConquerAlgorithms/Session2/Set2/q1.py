# Problem 1: Finding the Perfect Song
# Abby Lee of Dance Moms is looking for the perfect song to choreograph a group routine to and needs a song of a specified length. Given a specific song length length and a list of song lengths playlist sorted in ascending order, use the binary search algorithm to return the index of the song in playlist with length. If no song with the target length exists, return -1.

def find_perfect_song(playlist, length):
    def binary_search(left, right):
        if left > right:
            return -1
        
        mid = (left + right) // 2
        if playlist[mid] == length:
            return mid
        elif playlist[mid] > length:
            return binary_search(left, mid - 1)
        else:
            return binary_search(mid + 1, right)
    
    return binary_search(0, len(playlist) - 1)
# Example Usage:

print(find_perfect_song([101, 102, 103, 104, 105], 103))
print(find_perfect_song([201, 202, 203, 204, 205], 206))
2
-1