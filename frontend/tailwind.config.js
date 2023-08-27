/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
    theme: {
        extend: {
            fontFamily: {
                jost: ["Jost", "sans-serif"],
                sans: ["DM Sans", "sans-serif"],
            },
            colors: {
                "secondary-btn": "rgba(24, 119, 242, 0.1)",
                "card-bg": "#F4F5F7",
                primary: {
                    disabled: "rgba(239, 159, 39, 0.5)",
                    red: "#EF9F27",
                    white: "#FFFFFF",
                    black: "#000000",
                },

                green: {
                    500: "#064",
                    400: "#00875A",
                    300: "#36B37E",
                    200: "#57D9A3",
                    100: "#79F2C0",
                    75: "#ABF5D1",
                    50: "#E3FCEF",
                },
                neutral: {
                    400: "#505F79",
                    300: "#5E6C84",
                    200: "#6B778C",
                    100: "#7A869A",
                    90: "#8993A4",
                    80: "#97A0AF",
                    70: "#A5ADBA",
                    60: "#B3BAC5",
                    50: "#C1C7D0",
                    40: "#DFE1E6",
                    30: "#EBECF0",
                    0o1: "#FAFBFC",
                    0o0: "#FFFFFF",
                },
            },
            height: {
                100: "25rem",
            },
            fontSize: {
                "title": "4rem",
            },
            translate: {
                "-104": "-26rem",
            },
        },
    },
    variants: {
        extend: {},
    },
    plugins: [],
};

