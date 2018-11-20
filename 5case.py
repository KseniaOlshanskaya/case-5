import urllib.request

with open('input.txt', 'r') as urls:
    with open("output.txt", "w") as output:
        print("{:<20s} {:<7s} {:<7s} {:<7s} {:<7s} {:<7s} "
              "{:<7s}".format("Player name", "COMP", "ATT", "YDS", "TD", "INT", "PR"), file=output)
        print("\n", file=output)
        for url in urls:
            if url.startswith("п»ї"):
                url = url.replace("п»ї", "")

            f = urllib.request.urlopen(url)
            s = f.read()
            text = str(s)

            part_name = text.find("player-name")
            name = text[text.find('>', part_name) + 1:text.find('&', part_name)]

            part_total = text.find("player-totals")
            total = text[text.find('<td>', part_total):text.find('</table>', part_total)]

            player_totals = str(total)
            editing = player_totals.replace('<td>', '')
            editing = editing.replace('</td>', ' ')
            editing = editing.replace('</tr>', '')
            editing = editing.replace('n', '')
            editing = editing.replace('t', '')
            editing = editing.replace(',', '.')
            _str = ''

            for c in editing:
                if c.isdigit() or c == '.' or c == ' ':
                    _str += c

            f = _str.split(' ')
            ATT = f[1]
            COMP = f[0]
            YDS = f[3]
            TD = f[5]
            INT = f[6]
            PR = f[9]
            print("{:<20s} {:<7s} {:<7s} {:<7s} {:<7s} {:<7s} "
                  "{:<7s}".format(name, COMP, ATT, YDS, TD, INT, PR), file=output)
