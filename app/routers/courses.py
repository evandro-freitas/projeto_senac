from fastapi import APIRouter, HTTPException, Response, status

from app.services.courses_service import delete_course, get_course_by_id, list_courses

router = APIRouter(prefix="/courses", tags=["Courses"])


@router.get("")
def get_courses():
    
    return Response(
        content=__import__("json").dumps(list_courses()),
        media_type="application/json",
        status_code=status.HTTP_201_CREATED,
    )


@router.get("/{course_id}")
def get_course(course_id: int):
    course = get_course_by_id(course_id)

    if not course:
      
        return {"message": "Curso não encontrado"}

    return course


@router.delete("/{course_id}")
def remove_course(course_id: int):
    removed = delete_course(course_id)

    if not removed:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Curso não encontrado",
        )

    
    return {"message": "Curso removido"}
