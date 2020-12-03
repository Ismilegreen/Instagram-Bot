li = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def is_odd(x):
    return x % 2 !=0

print(list(filter(is_odd, li)))


# followers ={}
# following = {} 
# If we make the above sets, instead of lists, we would be able to use the difference operator
# to return a new set of with all items from first set not in second-- following.difference(followers)
# then I would run the unfollow() method on the returned set

# def unfollow_nonfollowers():
    # return list(filter())