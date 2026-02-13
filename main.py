"""Main module."""

import streamlit as st


def main():
    """Main."""
    st.title("Hello Michael.")

    st.markdown(
        """
        Hello Michael,,

        So nice, to see,,, you,.
        """
    )

    if st.button("Send balloons!"):
        st.balloons()


if __name__ == "__main__":
    main()
