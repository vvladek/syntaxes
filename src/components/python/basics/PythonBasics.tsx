

export function PythonBasics () {
    return(
        <section>
            <h1>Python Basics</h1>
            <div>
                <h2>Checking Python version</h2>
                <p>Enter the following command in the terminal.</p>
                <pre>{"python --version"}</pre>
            </div>
            <div>
                <h2>Displaying data on the screen</h2>
                <p>Function <strong>print</strong> helps display information in the console.</p>
                <pre>{"print(\"Hello world\")\nprint(1)"}</pre>
            </div>
            <div>
                <h2>Comments</h2>
                <p>Comments can be single-line or multi-line.</p>
                <pre>{"# comment\n\"\"\"\ncomment on the first line\ncomment on the second line\n\"\"\""}</pre>
            </div>
            <div>
                <h2>Variables</h2>
                <p>The variable can consist of Latin letters, numbers and underscores. In Python, we simply write the name of a variable, and use <strong>=</strong> operator to indicate its value.</p>
                <pre>{"a = 1\nb = \"Hello world\"\ngood_naming_practice = \"snake_case\""}</pre>
            </div>
            <div>
                <h2>Mathematical operations with numbers</h2>
                <p>You can do all the basic math in Python.</p>
                <pre>{"a = 1 + 2          # 3\nb = 2 - 1          # 1\nc = 4 * 2          # 8\nd = 8 / 2          # 4\ne = 10 // 3        # 3\nf = a + b          # 4\ng = 2 + 2 * 2      # 6\nh = (2 + 2) * 2    # 8\ni = -a             # -3\nj = 0.5 + 0.5      # 1.0\nk = 10 % a         # 1\nl = 2 ** 3         # 8\nm = 2 * 2 ** 3     # 16 (First exponentiation)"}</pre>
            </div>
            <div>
                <h2>Strings</h2>
                <p>Basic Python capabilities for working with strings.</p>
                <pre>{"str1 = \"Hello\"\nstr2 = \"world\"\nprint(str1 + \" \" + str2)  # Hello world\nprint(3 * str1)           # HelloHelloHello\nprint(str1[2])            # \"l\" is 2 char (0,1,2 ...)\nprint(str1[-1])           # \"o\" is last char\nprint(\"sfgs\\\"sdf\")        # sfgs\"sdf\nprint(len(str1))          # 5 is str1 length\nstr3 = \"\"\"\n  Python\n  has multi-line\n  strings.\n\"\"\""}</pre>
            </div>
            <div>
                <h2>Boolean values and None</h2>
                <p>Boolean value has only two options - <strong>True</strong> or <strong>False</strong>. Python also has another special value <strong>None</strong> which means “nothing.”</p>
                <pre>{"is_earth_flat = True\nis_earth_round = False\na = None\nprint(a)    # None"}</pre>
            </div>
            <div>
                <h2>Strong typing and basic type conversions</h2>
                <p>Python has strong object typing. You cannot directly interact with objects of different types. You need to convert both objects to the same type.</p>
                <pre>{"num = 12\nstr1 = \"ab\"\nprint(num + str1)            # Error\nprint(str(num) + str1)       # 12ab\nprint(int(\"1\") + int(\"2\"))   # 3\nprint(float(12))             # 12.0\ns = \"123\"\nprint(s[0] + s[1])           # 12 as (\"1\"+\"2\")\nprint(int(s[0]) + int(s[1])) # 3"}</pre>
            </div>
            <div>
                <h2>input Function</h2>
                <p><strong>input</strong> function allows you to enter data into the console, as well as save it for use in future work. In its optional parameter, you can pass a string with a request for the user. After running the code, the field to the right of the line allows the user to enter data. To save the entered data, you need to press the Enter key. The function returns a string as its result.</p>
                <pre>{"a = input(\"enter num: \") # Imagine that 42 is entered\nprint(a)                 # 42\nprint(a + 1)             # Error\nprint(int(a) + 1)        # 43"}</pre>
            </div>
        </section>  
    )
}