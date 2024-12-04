
def review(rating):

    assert rating>0,"too low"

    assert rating<0,"too high"

review(-1)

print("rated")