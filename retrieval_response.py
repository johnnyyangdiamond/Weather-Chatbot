from collections import Counter
from responses import responses, blank_spot
from retrieval_helper_functions import preprocess, compare_overlap, pos_tag, extract_nouns, compute_similarity
import spacy
word2vec = spacy.load('en_core_web_lg')

exit_commands = ("quit", "goodbye", "exit", "no")

class Retrieval_Response:
  
  def find_similarity(self, user_message):
    bow_user_message = Counter(preprocess(user_message))
    processed_responses = [Counter(preprocess(response)) for response in responses]
    similarity_list = [compare_overlap(doc, bow_user_message) for doc in processed_responses]
    return similarity_list

  def should_generate_response(self, user_message):
    similarity_list = self.find_similarity(user_message)
    if(max(similarity_list) < 1):
        return True
    else: 
        return False
  
  def find_intent_match(self, user_message):
      similarity_list = self.find_similarity(user_message)
      response_index = similarity_list.index(max(similarity_list))
      return responses[response_index]
 
  def find_entities(self, user_message):
      tagged_user_message = pos_tag(preprocess(user_message))
      message_nouns = extract_nouns(tagged_user_message)
      print(message_nouns)
      tokens = word2vec(" ".join(message_nouns))
      category = word2vec(blank_spot)
      word2vec_result = compute_similarity(tokens, category)
      word2vec_result.sort(key=lambda x: x[2])
      if len(word2vec_result) < 1:
         return blank_spot
      else:
         return word2vec_result[-1][0]
 
  def respond(self, user_message):
    best_response = self.find_intent_match(user_message)
    entity = self.find_entities(user_message)
    print(best_response.format(entity))
    input_message = input("Do you have any other questions? ")           
    return input_message

