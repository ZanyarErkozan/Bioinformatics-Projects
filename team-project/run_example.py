"""Örnek kullanım scripti - İlişki analizi.""" from analyze_family_tree import extract_relationship, NoSuchPersonError, IdenticalPersonError
import family1_config # Test edilecek kişi çiftleri
test_cases = [ ("T19_F1_XX16", "T19_F1_XY24", "unrelated"), ("T19_F1_XX19", "T19_F1_XX18", "unrelated"), ("T19_F1_XY22", "T19_F1_XX18", "first_cousins"), ("T19_F1_XY24", "T19_F1_XX18", "first_cousins_once_removed"), ("T19_F1_XY24", "T19_F1_XY15", "greatuncle_greatnephew"), ("T19_F1_XX46", "T19_F1_XY15", "uncle_niece"),
] print("=" * 70)
print("Forensic DNA Kinship Project - Phase 1")
print("Iliski Analizi Sonuclari")
print("=" * 70)
print() for person_a, person_b, expected in test_cases: try: relationship = extract_relationship(person_a, person_b, family1_config) status = "[OK]" if relationship == expected else "[X]" print(f"{status} {person_a:20} <-> {person_b:20} : {relationship:30}") if relationship != expected: print(f" (Beklenen: {expected})") except NoSuchPersonError as e: print(f"[X] {person_a:20} <-> {person_b:20} : HATA - Kisi bulunamadi") except IdenticalPersonError as e: print(f"[X] {person_a:20} <-> {person_b:20} : HATA - Ayni kisi") except Exception as e: print(f"[X] {person_a:20} <-> {person_b:20} : HATA - {e}") print()
print("=" * 70)
print("Test tamamlandı!")
print("=" * 70) 