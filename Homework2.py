from sys import argv


def find_gc_content(sequence):
    return round((sequence.count('G') + sequence.count('C')) / len(sequence) * 100)


def fastq_to_csv(inp, outp, lower_gc_content_bound, upper_gc_content_bound, gc_content_values=None):
    '''

    :param inp:
    :param outp:
    :param lower_gc_content_bound:
    :param upper_gc_content_bound:
    :param gc_content_values:
    :return:
    '''

    #try:
    #    lower_gc_content_bound = int(lower_gc_content_bound)
    #    upper_gc_content_bound = int(upper_gc_content_bound)
    #except TypeError:
    #    pass

    print(lower_gc_content_bound, upper_gc_content_bound, gc_content_values)
    with open(inp, 'r') as inp_file, open(outp, 'w') as outp_file:
        if gc_content_values:
            for line in inp_file:
                name = line.strip()
                seq = next(inp_file).strip()
                next(inp_file)
                next(inp_file)
                gc_content = find_gc_content(seq)
                if gc_content in gc_content_values:
                    outp_file.write('{}\t{}\t{}\n'.format(name, len(seq), gc_content))
        else:
            for line in inp_file:
                name = line.strip()
                seq = next(inp_file).strip()
                next(inp_file)
                next(inp_file)
                gc_content = find_gc_content(seq)
                if lower_gc_content_bound <= gc_content <= upper_gc_content_bound:
                    outp_file.write('{}\t{}\t{}\n'.format(name, len(seq), gc_content))


def getopts(argv):
    opts = {}
    it = iter(argv)
    g_arg_just_filled = False
    while True:
        try:
            if not g_arg_just_filled:
                val = next(it)
            else:
                g_arg_just_filled = False

            if val == '-g':
                g_arg_just_filled = True
                opts['-g'] = []
                val = next(it)
                while val[0] != '-':
                    opts['-g'].append(int(val))
                    val = next(it)
            elif val[0] == '-':
                opts[val] = next(it)

        except StopIteration:
            break

    return opts


def getopts_v2(argv):
    opts = {}
    it = iter(argv)
    val = next(it)
    while True:
        try:
            if val == '-g':
                opts['-g'] = []
                val = next(it)
                while val[0] != '-':
                    opts['-g'].append(int(val))
                    val = next(it)

            elif val[0] == '-':
                opts[val] = next(it)
                val = next(it)

        except StopIteration:
            break

    return opts

#getopts(['-i','ibp.txt','-g','55','66','-a','55'])
##getopts_v2(['-i','ibp.txt','-g','55','66','-a','55'])
#getopts_v2(['-i','ibp.txt','-a','55','-g','55','66'])

if __name__ == '__main__':
    opts = getopts(argv)
    print(opts)
    fastq_to_csv(opts['-i'], opts['-o'], opts.get('-a', 35), opts.get('-b', 45), opts.get('-g'))
