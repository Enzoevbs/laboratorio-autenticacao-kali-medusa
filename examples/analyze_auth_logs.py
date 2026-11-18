#!/usr/bin/env python3
"""Summarize synthetic authentication events from a local CSV file."""

import csv
from collections import Counter, defaultdict
from pathlib import Path


LOG_FILE = Path(__file__).with_name("auth_events.csv")
FAILURE_THRESHOLD = 3


def main():
    failures = Counter()
    accounts = defaultdict(set)
    sources_with_failures = set()
    successes_after_failures = set()

    with LOG_FILE.open(newline="", encoding="utf-8") as file:
        for event in csv.DictReader(file):
            key = (event["service"], event["source_ip"])
            username = event["username"]
            result = event["result"].strip().lower()

            if result == "failure":
                failures[key] += 1
                accounts[key].add(username)
                sources_with_failures.add(key)
            elif result == "success" and key in sources_with_failures:
                successes_after_failures.add((key, username))

    for (service, source_ip), count in sorted(failures.items()):
        if count >= FAILURE_THRESHOLD:
            print(
                "ALERTA: {} falhas | serviço={} | origem={} | contas={}".format(
                    count, service, source_ip, len(accounts[(service, source_ip)])
                )
            )

    for (service, source_ip), username in sorted(successes_after_failures):
        print(
            "REVISAR: sucesso após falhas | serviço={} | origem={} | usuário={}".format(
                service, source_ip, username
            )
        )

    if not failures:
        print("Nenhuma falha encontrada no arquivo.")


if __name__ == "__main__":
    main()
