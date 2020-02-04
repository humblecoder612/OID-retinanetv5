# OID-retinanetv5
OID v5 challenge 2019 - Retinenet - fizyr implementation

clone fizyr repositry :

by terminal command:

1.git clone https://github.com/fizyr/keras-retinanet.git

3.place images in sample folder and csv files in root directory

4. run csv maker script

5. run csv split script for training into batches

6.Open the jupyter notebook from there you can do every action step by step

                                                                OR 

6.cd keras-retinanet/

7. pip install .

8.python setup.py build_ext --inplace

9.python keras_retinanet/bin/train.py --freeze-backbone --random-transform --weights ./snapshots/weigthfile --batch-size 5 --steps 895 --epochs 10 csv ../anotcsvfile ../classcsvfile

or you can 
