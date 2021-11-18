{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7f65dbd0-0ec3-4223-9c14-3b2b822e01fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "records =[]\n",
    "#row_count = 0\n",
    "\n",
    "\n",
    "with open(csvpath,'r') as csvfile :\n",
    "    csvreader = csv.reader(csvfile, delimiter=',')\n",
    "    csv_header = next(csvreader)\n",
    "    csv_header.append(\"Diff\")\n",
    "    records.append(csv_header)\n",
    "    cum_pl_t0 = 0\n",
    "    cum_pl_t1 = 0\n",
    "    ls_avg = []\n",
    "    for row in csvreader:\n",
    "        date = row[0]\n",
    "        p_l = int(row[1])\n",
    "        if row.index == 1:\n",
    "            cum_pl_t0 = 0\n",
    "            cum_pl_t1 = p_l\n",
    "        else :\n",
    "            cum_pl_t0 = cum_pl_t1\n",
    "            cum_pl_t1 = cum_pl_t1 + p_l\n",
    "        ls_avg.append(cum_pl_t1 - cum_pl_t0)\n",
    "        \n",
    "        "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
