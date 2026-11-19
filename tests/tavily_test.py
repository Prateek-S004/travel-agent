from backend.tools.tavily_tool import websearch


def main():
    result = websearch.invoke({
        "source": "Hubballi",
        "destination": "Bengaluru"
    })

    print("\n========== TAVILY SEARCH RESULTS ==========\n")
    print(result)
    print("\n============================================")


if __name__ == "__main__":
    main()