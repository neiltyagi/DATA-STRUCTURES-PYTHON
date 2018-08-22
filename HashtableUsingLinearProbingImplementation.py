{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n"
     ]
    }
   ],
   "source": [
    "class Hashtable:\n",
    "    def __init__(self):\n",
    "        self.size=10\n",
    "        self.key=[None]*self.size\n",
    "        self.value=[None]*self.size\n",
    "        \n",
    "    def hashfunction(self,key):\n",
    "        sum=0\n",
    "        for pos in range(len(key)):\n",
    "            sum=sum+ord(key[pos])\n",
    "            \n",
    "        return sum%self.size\n",
    "\n",
    "#insert method    \n",
    "# first we assume that collision occured so we loop until we find an emptyplace\n",
    "#while looping we also check weather that key already exist \n",
    "#if yes we update the value and exit\n",
    "#We loop according to linear probing implementation and increment the index by 1\n",
    "#when we come out of while (without invoking return present inside )it means \n",
    "#we have reached an empty space and we update the value    \n",
    "    \n",
    "    def insert(self,key,data):\n",
    "        index=self.hashfunction(key)\n",
    "\n",
    "        while self.key[index] != None:\n",
    "            if self.key[index]==key:\n",
    "                self.value[index]=data\n",
    "                return\n",
    "            \n",
    "            index=(index+1)%self.size\n",
    "            \n",
    "        self.key[index]=key\n",
    "        self.value[index]=data\n",
    "            \n",
    "    def get(self,key):\n",
    "        index=self.hashfunction(key)\n",
    "        \n",
    "        while self.key[index] != None :\n",
    "            if self.key[index]==key:\n",
    "                return self.value[index]\n",
    "            index=(index+1)%self.size\n",
    "            \n",
    "        return None\n",
    "        \n",
    "        \n",
    "table=Hashtable()\n",
    "table.insert('apple',10)\n",
    "table.insert('orange',20)\n",
    "table.insert('car',30)\n",
    "table.insert('table',40)\n",
    "print table.get('car')\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
