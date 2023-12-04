# API Design Challenge

## Purpose

The intended purpose of this challenge is to evaluate your approach to API design. We're interested in seeing how you approach this kind of problem philosophically and pragmatically.

# Problem

You've inherited an API that serves up some model (`rpc1`) to some unspecified clients. We've just come up with a new and improved model (`rpc2`) that serves up slightly different responses.

## What would you do to introduce the new model to the API?

As with most things, it depends.

Some factors to consider are what, if anything, was expressed to API consumers beforehand,
how many clients are using the API,
can we communicate with them,
can we guarantee or monitor certain kinds of usage, or
potentially other things that we find out in search of these answers.

If we can determine that there are only a few clients,
and we are in control of their code,
we may be able to easily check their usage
and make updates as necessary for `rpc2`.

Given the use of FastAPI and it's ability to publish the OpenAPI specs for something like Swagger UI,
consumers of the API could have seen the Pydantic schemas for the request and response.

Since that response just states that there is a list of predictions,
it can be fair to say that there doesn't need to be any additional communication
as the changes in `rpc2` still conform to that specification.

If clients always assumed there'd only be two labels: `foo` and `bar`,
it'd be best to have communicated this earlier and potentially have something logged out.

To be extra safe that existing clients don't have any breakage,
we can either version the API with a version 2 having additional labels like `baz`,
or allow for an optional parameter in the existing endpoint that only use `rpc2`
if, for example, an `extra_labels` flag is set to `True`.

If there's a lot of usage by unreachable clients,
we can publish a deprecation notice, warnings, and errors over time.
At first, it may be a small percentage of requests,
and later on it can increase to all requests to the old endpoint.

## What (if anything) would you have done differently in the initial design to prepare for this event? Please make the code changes necessary to introduce the version, and provide the documentation needed for new and existing consumers to adapt.

Again, it would depend.

If we estimated there only be a low usage,
it might've been best to move quickly to test out ideas for the business to gain traction on what is the best product.

If we knew there would be high usage,
we could've been more strict in declaring the response schema to only have certain labels,
or express in the documentation that there may be additional labels other than `foo` and `bar` in the future.

Given that this seems like an endpoint that's making predictions with different labels and weights for a given message,
I'd think that clients would want the best prediction possible over time.
This is especially true since it was not previously documented, in the API,
that there would be certain labels at all.

Because of this, I'd leave the response schemas broad to accommodate for improved labels in the future,
while also making it stricter to note that the predictions actually have a `label` and `weight`.
I would more clearly express this in the API documentation
so that clients could understand this more as they initially develop with the API.

See [./main.py](./main.py) for these, some minor edits,
and tests to automatically ensure these are enforced in continuous integration.
