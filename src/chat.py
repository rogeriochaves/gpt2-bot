#!/usr/bin/env python3

import fire
import json
import os
import sys
import numpy as np
import tensorflow as tf

import model
import sample
import encoder

model_name = '117M'
seed = None
length = 200
temperature = 10
top_k = 5


def load_model():
    enc = encoder.get_encoder(model_name)
    hparams = model.default_hparams()
    with open(os.path.join('models', model_name, 'hparams.json')) as f:
        hparams.override_from_dict(json.load(f))

    if length > hparams.n_ctx:
        raise ValueError(
            "Can't get samples longer than window size: %s" % hparams.n_ctx)

    sess = tf.Session(graph=tf.Graph()).__enter__()
    # with  as sess:
    np.random.seed(seed)
    tf.set_random_seed(seed)
    context = tf.placeholder(tf.int32, [1, None])
    output = sample.sample_sequence(
        hparams=hparams, length=length,
        context=context,
        batch_size=1,
        temperature=temperature, top_k=top_k
    )

    saver = tf.train.Saver()
    ckpt = tf.train.latest_checkpoint(
        os.path.join('models', model_name))
    saver.restore(sess, ckpt)
    print("done")

    return sess, enc, context, output


def bot_reply(model, conversation):
    sess, enc, context, output = model

    encoded_conversation = enc.encode(conversation)
    result = sess.run(output, feed_dict={
        context: [encoded_conversation]
    })[:, len(encoded_conversation):]
    text = enc.decode(result[0])

    splits = text.split('\n')
    reply = splits[0]

    return reply


def interact_model(
    conversation="""
— John Doe: Hello, what is your name?
— Consultant: My name is Consultant, how can I help you?"""
):
    model = load_model()

    print(conversation)

    while True:
        message = None
        while not message:
            message = input("— John Doe: ")
        conversation += "\n— John Doe: " + message
        conversation += "\n— Consultant:"
        sys.stdout.write("— Consultant:")
        sys.stdout.flush()

        reply = bot_reply(model, conversation)

        sys.stdout.write(reply+'\n')
        sys.stdout.flush()
        conversation += reply


if __name__ == '__main__':
    fire.Fire(interact_model)
