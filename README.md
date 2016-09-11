# Readme Guidelines for Challenges

All of the README.md files of challenge repositories should be written along these rules.

## Structure

The basic structure is:

``` markdown
# {Challenge Name}

*This is a [codecheck](https://app.code-check.io/openchallenges) challenge. To get started, [see the docs](https://code-check.github.io/docs/en)* :-)  

{background information of the challenge. Write clearly, but with humor.}

## Your Mission
{the required result of the challenge}

## Implementation
{implementation details of the challenge.  may include information about
 CLI app implementation, tests, input parameters, etc.}

## Answer.md
In [answer.md](answer.md) write a brief explanation about:
- How your code works
- Problems faced while solving the challenge
- How you solved those problems
```

- Make the outline only one level deep (uses only `##` for headers).
- Only if absolutely necessary, use `#####` for the second level header to make the depth absolutely clear.
- Levelling beyond the third level is prohibited! :angry-kuririn:
- A good example is the [look-and-say](https://github.com/givery-technology/look-and-say) challenge.

## CLI Applications

For CLI App Challenges, include the below section in `## Implementation`:

``` markdown
##### CLI
Build the solution as a CLI application that receives arguments from `stdin` and returns the expected output to `stdout`.  
See [YOUR_LANGUAGE].md for details on how to build a CLI application.
You can use the following languages to solve this challenge.

- {list languages here}
- ...

```
## Language

- The English readme belongs in `README.md`
- The Japanese readme belongs in `README_ja.md`
