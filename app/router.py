from fastapi import APIRouter, Request, Response
from fastapi import File, UploadFile
import traceback

import service

router = APIRouter()

@router.get('/')
async def root():
    return 'service up'

@router.get('/get_recommendations')
async def get_recommendations(request: Request, response: Response, cve_id: str):
    try:

        async with request.app.state.desc_sem:
            parse_result = await service.parse_description(cve_id)
        if parse_result['status'] == 'error':
            response.status_code = 500
            return {"message": f"Error while getting CVE description: {parse_result['cause']}"}
        
        description = parse_result['result']
        async with request.app.state.model_sem:
            answer = await service.get_recommendations(request.app.state.model, cve_id, description)

        return {'answer': answer}
    
    except Exception:

        response.status_code = 500
        traceback.print_exc()

        return {"message": "There was an unexpected error"}