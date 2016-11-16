from PythonCourse.Fastq import FastqRead

with open('/home/aleksandrsl/Desktop/BioinformaticInstitute/PythonCourse/FastqExample', 'r') as f:
    test_read_1 = FastqRead(f)
    print(test_read_1)
    print(test_read_1.name)
    print(test_read_1.sequence)
    print(test_read_1.quality)
    next(f)
    next(f)
    next(f)
    next(f)
    print(FastqRead.min_aver_qual)
    test_read_2 = FastqRead(f)
    print(test_read_2.seq_at(10000))
    print(test_read_2.qual_at(5))
    print(test_read_2[5])
    print(test_read_2.aver_qual())
    print(test_read_2.good())
    for seq, qual in test_read_2:
        print(seq, qual)
    # test_read_2.qual_at(100000)
    # test_read_2.qual_at(-1)
    FastqRead(f)
    empty_read = FastqRead(f)
    # print(empty_read) # Естетвенно вызывает ошибку, так как ничего не инициализировано, но я не очень представляю
    #     что делать в таких случаях

