import pytest
import numpy as np


# test the encode and decode funcs
black = np.zeros((100, 100, 3))
sum_black = np.sum(black)
white = np.ones((100, 100, 3))*255
sum_white = np.sum(white)


@pytest.mark.parametrize("img, expected", [
    (black, sum_black),
    (white, sum_white), ])
def test_encode_decode(img, expected):
    from encode_decode import imgArray2str
    from encode_decode import str2imgArray
    # turn to string and back to img array
    img_str = imgArray2str(img)
    imgback = str2imgArray(img_str)
    temp = imgback.copy()
    temp[:, :, 0] = imgback[:, :, 2]
    temp[:, :, 2] = imgback[:, :, 0]
    imgback = temp
    summa = np.sum(img)
    assert summa == expected
