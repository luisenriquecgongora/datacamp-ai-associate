from transformers import pipeline 

# Create a pipeline for grammar checking
grammar_checker = pipeline(
  task="text-classification",
  model="textattack/albert-base-v2-CoLA"
)

# model="abdulmatinomotoso/English_Grammar_Checker" //BETTER RESULTS

# Check grammar of the input text
output = grammar_checker("I will walk dog")
print(output)

print(grammar_checker.model.config.id2label)