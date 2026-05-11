from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a:int,b:int)->int:
    """_summary_

    Add two numbers

    Args:
        a (int): first
        b (int): second

    Returns:
        int: result
    """
    return a + b



@mcp.tool()
def multiple(a:int,b:int)->int:
    """_summary_
    Multipy two numbers
    Args:
        a (int): first
        b (int): second

    Returns:
        int: final result
    """
    return a*b



# The trasport="stdio" argument tells the server to:
# use the standard input/output (stdin and stdout) to receive and respond to tll function caslls

if __name__ == "__main__":
    mcp.run(transport="stdio")


    
