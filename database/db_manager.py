import json
import os
from typing import List, Dict, Optional
from config.config import STUDENTS_FILE, GRADES_FILE
from database.models import Student, Grade

class DatabaseManager:
    """Gestionnaire de base de données JSON"""
    
    @staticmethod
    def load_students() -> List[Dict]:
        """Charger tous les étudiants"""
        try:
            with open(STUDENTS_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get('students', [])
        except FileNotFoundError:
            return []
    
    @staticmethod
    def load_grades() -> List[Dict]:
        """Charger toutes les notes"""
        try:
            with open(GRADES_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get('grades', [])
        except FileNotFoundError:
            return []
    
    @staticmethod
    def get_student_by_id(student_id: str) -> Optional[Dict]:
        """Récupérer un étudiant par son ID"""
        students = DatabaseManager.load_students()
        for student in students:
            if student['id'] == student_id:
                return student
        return None
    
    @staticmethod
    def get_student_grades(student_id: str) -> List[Dict]:
        """Récupérer les notes d'un étudiant"""
        grades = DatabaseManager.load_grades()
        return [g for g in grades if g['student_id'] == student_id]
    
    @staticmethod
    def add_student(student: Student) -> bool:
        """Ajouter un étudiant"""
        try:
            students = DatabaseManager.load_students()
            if any(s['id'] == student.id for s in students):
                return False  # Existe déjà
            
            students.append(student.to_dict())
            
            with open(STUDENTS_FILE, 'w', encoding='utf-8') as f:
                json.dump({'students': students}, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"❌ Erreur: {e}")
            return False
    
    @staticmethod
    def add_grade(grade: Grade) -> bool:
        """Ajouter une note"""
        try:
            grades = DatabaseManager.load_grades()
            grades.append(grade.to_dict())
            
            with open(GRADES_FILE, 'w', encoding='utf-8') as f:
                json.dump({'grades': grades}, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"❌ Erreur: {e}")
            return False
    
    @staticmethod
    def calculate_average(student_id: str) -> float:
        """Calculer la moyenne générale"""
        grades = DatabaseManager.get_student_grades(student_id)
        if not grades:
            return 0
        
        total_points = sum(g['score'] * g['coefficient'] for g in grades)
        total_coefficients = sum(g['coefficient'] for g in grades)
        
        return round(total_points / total_coefficients, 2) if total_coefficients > 0 else 0
