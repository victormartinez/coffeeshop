# Coffee Shop AI

In this exercise we'd like you to build a small conversational AI for our imaginary coffee shop. This system will consist of two agents (the guest and the employee) that interact with each other through simple text messages. The guest agent will be given a list of sentences that they should speak, and the employee agent should act according to the requests of the user.

### Deliverables

The deliverable should be a command line application that takes as an input argument the path of a text file (or standard input) containing the list of sentences the guest should send, one for each line. It should then perform a simulation of the conversation, printing to standard output lines of the following format: "Guest: What the guest said.", and "Employee: What the employee said." The entire simulation must be implemented as a real-time system using asyncio, having a separate task for each agent.

Your implementation should be simple, elegant, and readable. If you encounter any missing details in the assignment instructions, it will be up to you to fill in the blanks. You are free to use any packages you like, as long as you build your application on top of asyncio.

### Menu

The coffee shop has the following items on the menu:

| Americano | $1.51 |
| --- | --- |
| Espresso | $1.27 |
| Latte | $2.13 |
| Macchiato | $3.39 |
| Tea | $1.75 |
| Cookie | $0.50 |

The coffee shop wants to make a healthy profit, so the manager has asked all employees to attempt to upsell a cookie whenever a guest orders a drink, but only if they haven't already ordered a cookie, and employees are only allowed to ask an upsell question once per conversation.

### Guest messages

The guest agent can say any of the following messages:

1. "I'd like a X." / "I'd like an X."
This is said when the guest wants to order a specific item on the menu.
2. "I don't want a X." / "I don't want an X."
This is said when the guest changed their mind about a previously ordered item.
3. "That's all."
This is said after the guest has finished ordering.
4. "Yes, please."
This is said when the guest wants to accept the cookie upsell.
5. "No, thank you."
This is said when the guest wants to reject the cookie upsell.

### Employee messages

The restaurant agent can say any of the following responses:

1. "Welcome to our coffee shop. What can I get you?"
This is said by the employee at the start of the conversation and signals to the guest that they can start ordering.
2. "Would you like anything else?"
After adding or removing an item from the order, this response is said to ask the guest for additional input.
3. "I don't understand."
Any message that the employee doesn't understand should get this response.
4. "Would you like to add a cookie for $X?" (may only be asked once after a drink and if no cookie was added yet)
This is the upsell message that should be sent as described above.
5. "Your total is $X. Thank you and have a nice day!"
After the guest finished ordering the employee should compute the total and finish the conversation.

### Example conversation

Employee: Welcome to our coffee shop. What can I get you?
Guest: I'd like an americano.
Employee: Would you like to add a cookie for $0.50?
Guest: Yes, please.
Employee: Would you like anything else?
Guest: That's all.
Employee: Your total is $2.01. Thank you and have a nice day!

You have three hours to complete the exercise. Good luck, and happy coding!

## Bonus: Handling indecisiveness

If you managed to get a working implementation of the task, and you have time remaining, then here is a bonus task, allowing you to earn some extra points!

It happens every once in a while that a guest comes to the coffee shop, but hasn’t fully decided yet what they would want. In such a case, the guest will tell the employee that they need some time to think, then wait a few seconds, and then continue the conversation. When the employee hears that the guest is thinking, they will request the guest to order when they are ready. However, guests should not take too long to decide. That is why for every ten seconds spent waiting the employee will repeat that the guest can order when they are ready.

Concretely, the following guest messages should be added to the system:

1. "Let me think."
This is said when the guest needs some time to think about what to order.
2. "WAIT N"
This message is not actually sent by the guest, but makes the guest agent wait for N seconds to simulate indecisiveness.

Additionally, the following employee responses should be added:

1. "Please let me know when you are ready."
If the guest indicated they needed some time to think, the employee should send this message. The employee should send this message again for every 10 seconds spent waiting for the guest.

An example conversation for the bonus could be as follows:

```
Guest: I'd like an americano.
Employee: Would you like a cookie for $0.50?
Guest: No, thank you.
Employee: Would you like anything else?
Guest: Let me think.
Employee: Please let me know when you are ready.
Guest: WAIT 5
Guest: That’s all.
Employee: Your total is $1.51. Thank you and have a nice day!
```