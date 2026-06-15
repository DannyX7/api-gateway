from .authenticationController import router as AuthenticationRouter
from .onboardingController import router as OnboardingRouter
from .learningController import router as LearningRouter
from .nodeProxyController import router as NodeProxyRouter

def init(app):
    app.include_router(AuthenticationRouter)
    app.include_router(OnboardingRouter)
    app.include_router(LearningRouter)
    app.include_router(NodeProxyRouter)
