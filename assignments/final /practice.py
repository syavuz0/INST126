{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "58c65ebe-173d-4fdc-b5cd-dc2cb4eb7fd5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    this is a bunch of nonsense text that im using...\n",
       "dtype: object"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from pandas import Series, DataFrame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9116f3d1-86a2-4379-8cc4-67dbe9b50037",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from pandas import Series, DataFrame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3dff65da-aedc-4fc5-b2b0-1d4cedc1571a",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    this is a bunch of nonsense text that im using...\n",
       "dtype: object"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s = Series(\"this is a bunch of nonsense text that im using to get a better understanding of regular expressions\")\n",
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "69c74463-2d04-446b-b98f-9f2dc3019a9f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    this is a bunch of nonsense text that im using...\n",
       "dtype: object"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.loc[s.str.contains('i')] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8383dcef-0ba4-44ac-8141-2d2318ff983a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
