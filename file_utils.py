from collections import defaultdict


def read_config_file(file_in):
    """
    Read config file specifying all needed parameters
    :param file_in: 
    :return: 
    """
    config_data = dict()
    with open(file_in) as read_in:
        for line in read_in:
            splitted_line = line.strip().split(':')
            config_data[splitted_line[0]] = splitted_line[1].strip()

    return config_data


def read_go_annotations(file_in):
    """
    Read known GO annotations from file
    :param file_in: 
    :return: 
    """
    go_annotations = defaultdict(set)

    with open(file_in) as read_in:
        for line in read_in:
            splitted_line = line.strip().split()
            identifier = splitted_line[0]
            go_terms = set(splitted_line[1].split(','))

            go_annotations[identifier] = go_terms

    return go_annotations


def write_predictions_cafa(predictions, out_file, model_num):
    """
    Write prediictions in CAFA format
    :param predictions: predictions to write
    :param out_file: output file
    :param model_num: number of model that is used
    :return:
    """
    with open(out_file, 'w') as out:
        out.write('AUTHOR\tRostlab2\nMODEL\t{}\nKEYWORDS\thomolog, machine learning, natural language processing.'
                  '\n'.format(model_num))
        for p in predictions.keys():
            prediction = predictions[p]
            for pred in prediction.keys():
                ri = prediction[pred]
                out.write('{}\t{}\t'.format(p, pred))
                out.write('{:0.2f}\n'.format(float(ri)))
        out.write('END')


def write_predictions(predictions, out_file):
    """
    Write predictions in the format 'target GO term    RI'
    :param predictions: predictions to write to file
    :param out_file: file to write predictions to
    :return: 
    """
    with open(out_file, 'w') as out:
        out.write('Target ID\tGO Term\tRI\n')
        for p in predictions.keys():
            prediction = predictions[p]
            for pred in prediction:
                ri = prediction[pred]
                out.write('{}\t{}\t'.format(p, pred))
                out.write('{:0.2f}\n'.format(float(ri)))


def write_hits(hits, out_file):
    """
    Write identifier for hit found for a respective query
    :param hits: 
    :param out_file: 
    :return: 
    """
    with open(out_file, 'w') as out:
        out.write('Query\tHit\tRI\n')
        for q in hits.keys():
            h = hits[q]
            for k in h.keys():
                ri = h[k]
                out.write('{}\t{}\t{}\n'.format(q, k, ri))
