# sts
Simple text search test for interview

This repository contains the code I was asked to write as a test.

My approach to the task:

Examining the requirements I noted:
  command line python prog - so use argparse + re modules
  argument 1: directory path (single - so no lists of directories (phase 2 FR???))
  FR: read all text files -= how to identify text files? use file descriptor? use .txt suffix??
                                        assume .txt suffix
  FR: all structures to be in-memory (so no Whoosh or Lucerne here)
  NFR: looking for efficient indexing for searching (so numpy / pandas?)
  FR: loop over command prompt (so input()) - what terminates? ctrl-Z? empty input?
                                        assume empty input - nice and simple
  FR: multiple words on command prompt (so how separated? include whole phrase as-is? all single words?
                                        assume: space separated as per example given, not whole phrase - single words
                                        phase 2 - include quotes for word phrase e.g. "hamlet skull 'to be or not to be' \n" gives 3 tokens not 8
                                        what about case-sensitivity? no FR for it - assume no case unless flag set on command line   (--c)
FR: limit matching selections to max 10 (set column limit in pandas??? )
FR: order list by rank (so how to weight the results?
          FR: ranking: all words -> 100%; no words -> 0%; 
                           assume 1/2 of the words -> 50%
NFR: unit tests required - (so use pytest)
NFR: need a README with build and run instructions
