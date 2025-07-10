{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c6374c99-893b-4bc3-8b8a-c34d964e9647",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "def preprocess_input(df):\n",
    "    substance_map = {'carbon dioxide': 0, 'methane': 1, 'nitrous oxide': 2, 'other GHGs': 3}\n",
    "    unit_map = {'kg/2018 USD, purchaser price': 0, 'kg CO2e/2018 USD, purchaser price': 1}\n",
    "    source_map = {'Commodity': 0, 'Industry': 1}\n",
    "\n",
    "    df['Substance'] = df['Substance'].map(substance_map)\n",
    "    df['Unit'] = df['Unit'].map(unit_map)\n",
    "    df['Source'] = df['Source'].map(source_map)\n",
    "    return df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bdf84291-02c8-4cad-a13a-848f6168b98c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d2f91d92-36cf-4379-9c8b-750d8909d2ad",
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
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
