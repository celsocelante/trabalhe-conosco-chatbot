## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
  - utter_get_user_info
* deny
  - utter_goodbye

## order coffe: happy path
> check_user_form
* affirm
  - utter_order_coffe
* affirm or deny
  - order_form
  - form{"name": "order_form"}
  - form{"name": null}
  - utter_order_resume
> check_order_coffe

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
