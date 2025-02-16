n = int(input())
a = list(map(int, input().split()))

if len(a) < 2:
    print(len(a))
else:
    st = []

    for i in range(n):
        if len(st) > 1:
            b = st[-1]
            st.pop()
            c = st[-1]
            st.pop()
            if (b + c) % 2 != 0:
                st.append(c)
                st.append(b)
        st.append(a[i])

    if len(st) >= 2:
        b = st[-1]
        st.pop()
        c = st[-1]
        st.pop()
        if (b + c) % 2 != 0:
            st.append(c)
            st.append(b)

    print(len(st))